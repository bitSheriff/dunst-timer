# Maintainer: bitSheriff <root@bitsheriff.dev>
pkgname=dunst-timer
pkgver=1.00.02
pkgrel=1
pkgdesc="A Python script for setting timers with progress bar notifications in Dunst"
arch=('any')
url="https://github.com/bitSheriff/dunst-timer"
license=('MIT')
depends=('python' 'dunst')
source=("https://github.com/bitSheriff/dunst-timer/archive/v$pkgver.tar.gz")
sha256sums=('f77001d577b1b557605d27ea3da427231c447efad7c961fcde365f014a603254')

package() {
    install -Dm755 "$srcdir/$pkgname-$pkgver/dunst-timer.py" "$pkgdir/usr/bin/dunst-timer"
}
