# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global ext_id uBlock0@raymondhill.net

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{_datadir}/mozilla/extensions/%{firefox_app_id}

Name:           mozilla-ublock-origin
Version:        1.62.0
Release:        %autorelease
Summary:        An efficient blocker for Firefox

# Automatically converted from old format: GPLv3 and MIT and OFL and Unlicense - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-OFL AND Unlicense
URL:            https://github.com/gorhill/uBlock
Source0:        https://github.com/gorhill/uBlock/archive/%{version}/uBlock-%{version}.tar.gz
Source1:        mozilla-ublock-origin.metainfo.xml
Source2:        uAssets-%{version}.tar.gz
# uAssets tarball contains non-free filter lists
# thirdparties/mirror1.malwaredomains.com - http://www.malwaredomains.com/?page_id=1508
# thirdparties/pgl.yoyo.org - https://pgl.yoyo.org/license/
# generate a free one with the mktarball.sh script below
Source10:       uAssets-mktarball.sh
Patch0:         %{name}-nonfree.patch

Requires:       mozilla-filesystem
BuildArch:      noarch
# wabt doesn't work correctly on big-endian
ExcludeArch:    ppc64 s390x
BuildRequires:  binaryen
BuildRequires:  libappstream-glib
BuildRequires:  nodejs
BuildRequires:  python3
BuildRequires:  wabt
# lib/csstree https://github.com/csstree/csstree MIT
Provides:       bundled(npm-css-tree) = 2.2.1
# img/fontawesome/fontawesome-defs.svg http://fontawesome.io/ OFL
Provides:       bundled(fontawesome-fonts) = 4.7.0
# css/fonts/Inter/Inter-*.woff2 https://github.com/rsms/inter OFL
Provides:       bundled(inter-fonts)
# css/fonts/Metropolis/Metropolis-*.woff2 https://github.com/chrismsimpson/Metropolis Unlicense
Provides:       bundled(metropolis-fonts)
# lib/js-beautify https://github.com/beautify-web/js-beautify MIT
Provides:       bundled(js-beautify) = 1.14.7
# lib/punycode.js https://mths.be/punycode MIT
Provides:       bundled(js-punycode) = 1.3.2
# lib/diff https://github.com/Swatinem/diff LGPLv3
Provides:       bundled(js-github-swatinem-diff)
# lib/codemirror http://codemirror.net MIT
Provides:       bundled(js-codemirror) = 5.59.2
# lib/lz4 https://github.com/gorhill/lz4-wasm BSD
Provides:       bundled(lz4-wasm)
# lib/regexanalyzer https://github.com/foo123/RegexAnalyzer Copyleft
Provides:       bundled(js-regexanalyzer) = 1.2.0
# lib/hsluv https://github.com/hsluv/hsluv/ MIT
Provides:       bundled(js-hsluv) = 0.1.0
# usually much newer than Fedora's publicsuffix-list package
# easy to unbundle, but might affect security
# assets/thirdparties/publicsuffix.org/list/effective_tld_names.dat
Provides:       bundled(publicsuffix-list) = 20240504

%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and
enforce thousands more filters than other popular blockers out there.

Flexible, it's more than an "ad blocker": it can also read and create filters
from hosts files.

%prep
# https://github.com/gorhill/uBlock/tree/master/dist#build-instructions-for-developers
%setup -q -n uBlock-%{version}
mkdir -p dist/build/uAssets
tar -xz -C dist/build/uAssets -f %{SOURCE2}
pushd dist/build/uAssets/main
tools/make-ublock.sh
popd
%patch 0 -p1
rm src/{js/wasm,lib/{lz4,publicsuffixlist/wasm}}/*.wasm
mv src/css/fonts/Inter/LICENSE.txt LICENSE.Inter.txt
mv src/img/fontawesome/LICENSE.txt LICENSE.fontawesome.txt
mv src/lib/js-beautify/LICENSE LICENSE.js-beautify.txt
mv src/lib/codemirror/LICENSE LICENSE.codemirror.txt

%build
for d in src/{js/wasm,lib/{lz4,publicsuffixlist/wasm}} ; do
    pushd $d
        for f in *.wat ; do
            wat2wasm $f
        done
    popd
done
pushd src/lib/lz4
wasm-opt ./lz4-block-codec.wasm -O4 -o ./lz4-block-codec.wasm
popd
./tools/make-firefox.sh all

%install
install -Dpm644 dist/build/uBlock0.firefox.xpi %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi

install -Dpm644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE.txt
%license LICENSE.codemirror.txt
%license LICENSE.fontawesome.txt
%license LICENSE.js-beautify.txt
%license LICENSE.Inter.txt
%license src/css/fonts/Metropolis/UNLICENSE
%{firefox_inst_dir}/%{ext_id}.xpi
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
