# Maintainer: bitSheriff <root@bitsheriff.dev>
pkgname=dunst-timer
pkgver=1.0.0
pkgrel=1
pkgdesc="A Python script for setting timers with progress bar notifications in Dunst"
arch=('any')
url="https://github.com/bitSheriff/dunst-timer"
license=('MIT')
depends=('python')
source=("https://github.com/bitSheriff/dunst-timer/archive/v$pkgver.tar.gz")
sha256sums=('SKIP') # Replace with actual checksum or keep 'SKIP' for development

package() {
    install -Dm755 "$srcdir/$pkgname-$pkgver/dunst_timer.py" "$pkgdir/usr/bin/dunst_timer"
}
