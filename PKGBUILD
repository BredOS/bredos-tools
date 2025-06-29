# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-tools
pkgver=1.10.0
pkgrel=1
pkgdesc="A grand collection of tools"

arch=('any')
url="https://github.com/BredOS/bredos-tools"
license=('GPL3')

groups=(bredos)
depends=('python' 'arch-install-scripts' 'systemd' 'gcc')
optdepends=('dtc: Compile device trees with the dtsc helper')

source=('dtsc.py'
        'rkdump.sh'
        'bredos-chroot.sh'
        'lsmmc.py'
        'wakeupctl.py'
        'grub-password.sh'
        'grub-apply-unrestrict.py'
        'grub-unrestrict.hook'
        'sleepctl.py'
        'sleepctld'
        'sleepctl.service'
        'rkdump.1'
        'grub-password.1'
        'dtsc.1'
        'sleepctl.1'
        'sleepctld.1'
        'wakeupctl.1'
        'bredos-chroot.8')
sha256sums=('f264899c639e3e8897e2daaef00a035a85ab51e39ba9ae5bb32d31e41d5394eb'
            'b3a3fd7115f63180d466b05739b092912c8b62420e514f39cb36b2b345c11585'
            '3f8adbb46b4d0345ad558393ab66b4fa50d33c5761b742a513cf7aff803a94ee'
            '7fa338e127e816acf5fb6c04e47c8a6098a606929b3e068853281a00d85005e2'
            '12047c25a46a9e0def5cc687ed0d1690d8e80853680280d347b1102b5203bde3'
            'be81b089e5bb91a9a3c2ae6c6658d538ea2b031263e3ac9685be2c1ec87fba6f'
            'f430e73417126b2dcf84cfaa02b3fb5c520da5794faf8d29f9c8531ec970614e'
            'ffabbfbfdca391f8616340a4323eddb868040ca35c24bd8d7d6c5df3b2cc77ac'
            'b16aef713ffa13b9490b99a7919408671d7cbab1a109e1c5246367769711a6c8'
            'fff6d0aa5a19bb9ab39d1696d228d2685956fbcad5cadf1817b2b2e73cb4e87f'
            '7bde0bb9eb48c7c560194d04a0864c833e63662d3ff527a23844eaa0d1849101'
            'ccaab9ca8f25571d5809b82f7be9a7133d91a75c745ff7174d5c78c593510659'
            '99646c23b88b74fa6fa9220588cb7cc18b1782fa8642559ce237adfc8b98ef01'
            '9a3d90776fb514bbcbfdb8cef0034555c093906eeac6509d3faa460fe04d7371'
            'b0543503053367280b216f534941b39460a04461a5d19834ab679677275761c6'
            'bb1ff999bca9352af32caca4e92cfd5516954957dd9d4397b3f4bbcde26f8302'
            '13b871e82b556190e0f221caeb5b719b48355e908eacba1ab6ea863fb5e658e4'
            'ef25ee68d18f85fb9a9b8a1976fcdd55828fdc968a94cdeea78490c44680f6f6')

package() {
    # DTSC
    install -Dm755 "$srcdir/dtsc.py" "$pkgdir/usr/bin/dtsc"

    # RKDUMP
    install -Dm755 "$srcdir/rkdump.sh" "$pkgdir/usr/bin/rkdump"

    # Wakeupctl
    install -Dm755 "$srcdir/wakeupctl.py" "$pkgdir/usr/bin/wakeupctl"

    # BredOS-Chroot
    install -Dm755 "$srcdir/bredos-chroot.sh" "$pkgdir/usr/bin/bredos-chroot"

    # lsmmc
    install -Dm755 "$srcdir/lsmmc.py" "$pkgdir/usr/bin/lsmmc"

    # GRUB Password
    install -Dm755 "$srcdir/grub-password.sh" "$pkgdir/usr/bin/grub-password"
    install -Dm755 "$srcdir/grub-apply-unrestrict.py" "$pkgdir/usr/bin/grub-apply-unrestrict"
    install -Dm644 "$srcdir/grub-unrestrict.hook" "$pkgdir/usr/share/libalpm/hooks/grub-unrestrict.hook"

    # Sleepctl
    install -Dm755 "$srcdir/sleepctl.py" "$pkgdir/usr/bin/sleepctl"
    install -Dm755 "$srcdir/sleepctld" "$pkgdir/usr/bin/sleepctld"
    install -Dm644 "$srcdir/sleepctl.service" "$pkgdir/usr/lib/systemd/user/sleepctl.service"

    # Manual pages
    install -Dm644 "$srcdir/rkdump.1" "$pkgdir/usr/share/man/man1/rkdump.1"
    install -Dm644 "$srcdir/grub-password.1" "$pkgdir/usr/share/man/man1/grub-password.1"
    install -Dm644 "$srcdir/dtsc.1" "$pkgdir/usr/share/man/man1/dtsc.1"
    install -Dm644 "$srcdir/sleepctl.1" "$pkgdir/usr/share/man/man1/sleepctl.1"
    install -Dm644 "$srcdir/sleepctld.1" "$pkgdir/usr/share/man/man1/sleepctld.1"
    install -Dm644 "$srcdir/wakeupctl.1" "$pkgdir/usr/share/man/man1/wakeupctl.1"
    install -Dm644 "$srcdir/bredos-chroot.8" "$pkgdir/usr/share/man/man8/bredos-chroot.8"
}
