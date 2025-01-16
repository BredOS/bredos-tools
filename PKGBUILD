# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-tools
pkgver=1.0.0
pkgrel=1
pkgdesc="Scripts used for the development of BredOS"
arch=('any')
url="https://github.com/BredOS/bredos-tools"
license=('Unknown')
source=('dtsc' 'rkdump')
sha256sums=('c8f84dae31981c8e847f99a1f303f2b6924f721c56b93f138c4cf550bc714040'
            '773f008c45af861666a1384f072b2ffb6d00427632dd80b5d83d7fa2f6a66915')

package() {
    install -Dm755 "$srcdir/dtsc" "$pkgdir/usr/bin/dtsc"
    install -Dm755 "$srcdir/rkdump" "$pkgdir/usr/bin/rkdump"
}
