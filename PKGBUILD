# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-tools
pkgver=1.5.0
pkgrel=1
pkgdesc="A grand collection of tools"

arch=('any')
url="https://github.com/BredOS/bredos-tools"
license=('GPL3')

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
        'sleepctl.service')
sha256sums=('SKIP'
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
}
