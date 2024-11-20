# Maintainer: bitSheriff <root@bitsheriff.dev>
pkgname=dunst-timer
pkgver=1.00.01
pkgrel=1
pkgdesc="A Python script for setting timers with progress bar notifications in Dunst"
arch=('any')
url="https://github.com/bitSheriff/dunst-timer"
license=('MIT')
depends=('python' 'dunst')
source=("https://github.com/bitSheriff/dunst-timer/archive/v$pkgver.tar.gz")
sha256sums=('fbd06751394b348e0eb9ab8391ff7bf3d3fa18bf2ec49165deada62b3d54e11c')

package() {
    install -Dm755 "$srcdir/$pkgname-$pkgver/dunst-timer.py" "$pkgdir/usr/bin/dunst-timer"
}
