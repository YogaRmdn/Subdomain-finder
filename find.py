import requests
import time
import sys
from options.color import *
from options.header import header, clean
from tqdm import tqdm


def subdomain_find(domain, delay=3):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0 Safari/537.36"
        )
    }

    try:
        print(f"{BOLD_BLUE}[*]{RESET} Memulai scanning pada domain : {domain}...\n")
        time.sleep(0.5)

        try:
            with open("wordlist/subdomain_finder.txt", 'r') as file:
                subdomains = file.read().splitlines()
        except FileNotFoundError:
            print(f"{BOLD_RED}\n[!] Wordlist tidak ditemukan{RESET}")
            return

        with tqdm(total=len(subdomains), desc="Progress", ncols=80, colour="cyan") as pbar:
            for subdomain in subdomains:
                url = f"https://{subdomain}.{domain}"
                try:
                    respon = requests.get(url, headers=headers, timeout=3)
                    hasil = respon.status_code

                    if hasil < 400:
                        tqdm.write(f"{BOLD_GREEN}[✔]{RESET} {url:<40}{BOLD_GREEN}{hasil}{RESET}")
                    else:
                        tqdm.write(f"{BOLD_RED}[✘]{RESET} {url:<40}{BOLD_RED}{hasil}{RESET}")

                except requests.RequestException:
                    pass

                pbar.update(1)
                time.sleep(delay)

        print(f"\n{BOLD_GREEN}[+]{RESET} Scanning selesai bos")

    except KeyboardInterrupt:
        print(f"\n{BOLD_RED}[!] Tools dihentikan oleh user{RESET}")
        sys.exit()


if __name__ == "__main__":
    while True:
        try:
            clean()
            header()
            domain = input(f"{BOLD_BLUE}[?]{RESET} Domain target\t: ")
            delay = 1

            subdomain_find(domain, delay)

            tanya = input(f"\n{BOLD_BLUE}[?]{RESET} Ulangi proses pencarian? (y/n) : ")
            if tanya.lower() != "y":
                print(f"{BOLD_RED}[!] Keluar dari tools{RESET}")
                time.sleep(0.5)
                break

        except KeyboardInterrupt:
            print(f"\n{BOLD_RED}[!] Tools dihentikan oleh user{RESET}")
            break
