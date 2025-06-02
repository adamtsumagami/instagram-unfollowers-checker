import instaloader

def main():
    username = 'USERNAME_KAMU'  # Ganti dengan username kamu

    print(f"🔐 Loading session for {username}...")

    # Inisialisasi Instaloader dan muat sesi login
    L = instaloader.Instaloader()
    try:
        L.load_session_from_file(username)
        print("✅ Session loaded successfully.")
    except FileNotFoundError:
        print("❌ Session not found. Jalankan: instaloader --login=USERNAME terlebih dahulu.")
        return

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("📥 Mengambil daftar following...")
        followings = set(user.username for user in profile.get_followees())

        print("📤 Mengambil daftar followers...")
        followers = set(user.username for user in profile.get_followers())

        print(f"\n📊 Total Following: {len(followings)}")
        print(f"📊 Total Followers: {len(followers)}")

        not_following_back = sorted(followings - followers)

        print(f"\n🚫 Akun yang tidak follow balik ({len(not_following_back)}):")
        for user in not_following_back:
            print(f" - {user}")

    except Exception as e:
        print("❌ Terjadi kesalahan:", e)

if __name__ == "__main__":
    main()
