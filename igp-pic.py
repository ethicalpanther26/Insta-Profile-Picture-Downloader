import instaloader
ig = instaloader.Instaloader()
dp = input("Type your user name here:-")
ig.download_profile(dp, profile_pic_only=True)