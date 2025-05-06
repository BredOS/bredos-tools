# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-tools
pkgver=1.4.2
pkgrel=1
pkgdesc="Scripts used for the development of BredOS"
arch=('any')
url="https://github.com/BredOS/bredos-tools"
license=('GPL3')
depends=('python' 'arch-install-scripts')
optdepends=('dtc: Compile device trees with the dtsc helper')
source=('dtsc' 'rkdump' 'bredos-chroot' 'wakeupctl' 'grub-password' 'grub-apply-unrestrict' 'grub-unrestrict.hook')
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')
license=('Unknown')

package() {
    install -Dm755 "$srcdir/dtsc" "$pkgdir/usr/bin/dtsc"
    install -Dm755 "$srcdir/rkdump" "$pkgdir/usr/bin/rkdump"
    install -Dm755 "$srcdir/wakeupctl" "$pkgdir/usr/bin/wakeupctl"
    install -Dm755 "$srcdir/bredos-chroot" "$pkgdir/usr/bin/bredos-chroot"
    install -Dm755 "$srcdir/grub-password" "$pkgdir/usr/bin/grub-password"
    install -Dm755 "$srcdir/grub-apply-unrestrict" "$pkgdir/usr/bin/grub-apply-unrestrict"

    install -Dm644 "$srcdir/grub-unrestrict.hook" "$pkgdir/usr/share/libalpm/hooks/grub-unrestrict.hook"
}
