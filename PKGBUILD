# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-tools
pkgver=1.6.0
pkgrel=1
pkgdesc="A grand collection of tools"

arch=('any')
url="https://github.com/BredOS/bredos-tools"
license=('GPL3')

groups=(bredos)
depends=('python' 'arch-install-scripts' 'systemd')
optdepends=('dtc: Compile device trees with the dtsc helper')

source=('dtsc'
        'rkdump'
        'bredos-chroot'
        'wakeupctl.py'
        'grub-password'
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
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

package() {
    # DTSC
    install -Dm755 "$srcdir/dtsc" "$pkgdir/usr/bin/dtsc"

    # RKDUMP
    install -Dm755 "$srcdir/rkdump" "$pkgdir/usr/bin/rkdump"

    # Wakeupctl
    install -Dm755 "$srcdir/wakeupctl.py" "$pkgdir/usr/bin/wakeupctl"

    # BredOS-Chroot
    install -Dm755 "$srcdir/bredos-chroot" "$pkgdir/usr/bin/bredos-chroot"

    # GRUB Password
    install -Dm755 "$srcdir/grub-password" "$pkgdir/usr/bin/grub-password"
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
