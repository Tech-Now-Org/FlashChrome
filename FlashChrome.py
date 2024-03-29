import subprocess
import os
extension_path = #
def optimize_chrome():
    # Adjust Chrome settings and set process priority
    subprocess.run([
        "cmd", "/c",
        "start chrome.exe --disable-background-networking "
        "--disable-background-timer-throttling "
        "--disable-backgrounding-occluded-windows "
        "--disable-breakpad "
        "--disable-client-side-phishing-detection "
        "--disable-default-apps "
        "--disable-dev-shm-usage "
        "--disable-extensions "
        "--disable-features=site-per-process "
        "--disable-hang-monitor "
        "--disable-popup-blocking "
        "--disable-prompt-on-repost "
        "--disable-renderer-backgrounding "
        "--disable-sync "
        "--disable-translate "
        "--disable-web-resources "
        "--enable-automation "
        "--enable-logging=stderr "
        "--force-fieldtrials "
        "--ignore-certificate-errors "
        "--ignore-ssl-errors "
        "--load-extension=%s " % extension_path  # Add a space here
        "--log-level=0 "
        "--metrics-recording-only "
        "--mute-audio "
        "--no-default-browser-check "
        "--no-experiments "
        "--no-first-run "
        "--no-sandbox "
        "--no-service-autorun "
        "--no-user-gesture-required "
        "--safebrowsing-disable-auto-update "
        "--use-mock-keychain "
        "--disable-software-rasterizer "
        "--disable-gpu-vsync "
        "--disable-gpu "
        "--disable-gpu-compositing "
        "--enable-quic ; wmic process where name='chrome.exe' CALL setpriority 128"
    ], shell=True)

    print("Chrome optimization complete.")

if __name__ == "__main__":
    optimize_chrome()
