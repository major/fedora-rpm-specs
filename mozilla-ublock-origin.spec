# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global ext_id uBlock0@raymondhill.net

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{_datadir}/mozilla/extensions/%{firefox_app_id}

%global uAssets_commit 3cd137904ffe979f337f8e0099a46ca2d0c41e5f

Name:           mozilla-ublock-origin
Version:        1.44.4
Release:        1%{?dist}
Summary:        An efficient blocker for Firefox

License:        GPLv3 and MIT and OFL and Unlicense
URL:            https://github.com/gorhill/uBlock
Source0:        https://github.com/gorhill/uBlock/archive/%{version}/uBlock-%{version}.tar.gz
Source1:        mozilla-ublock-origin.metainfo.xml
Source2:        uAssets-%{uAssets_commit}.tar.gz
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
BuildRequires:  python3
BuildRequires:  wabt
# img/fontawesome/fontawesome-defs.svg http://fontawesome.io/ OFL
Provides:       bundled(fontawesome-fonts) = 4.7.0
# css/fonts/Inter/Inter-*.woff2 https://github.com/rsms/inter OFL
Provides:       bundled(inter-fonts)
# css/fonts/Metropolis/Metropolis-*.woff2 https://github.com/chrismsimpson/Metropolis Unlicense
Provides:       bundled(metropolis-fonts)
# lib/punycode.js https://mths.be/punycode MIT
Provides:       bundled(js-punycode) = 1.3.2
# lib/diff https://github.com/Swatinem/diff LGPLv3
Provides:       bundled(js-github-swatinem-diff)
# lib/codemirror http://codemirror.net MIT
Provides:       bundled(js-codemirror) = 5.59.2
# lib/lz4 https://github.com/gorhill/lz4-wasm BSD
Provides:       bundled(lz4-wasm)
# lib/regexanalyzer https://github.com/foo123/RegexAnalyzer Copyleft
Provides:       bundled(js-regexanalyzer) = 1.1.0
# lib/hsluv https://github.com/hsluv/hsluv/ MIT
Provides:       bundled(js-hsluv) = 0.1.0
# usually much newer than Fedora's publicsuffix-list package
# easy to unbundle, but might affect security
# assets/thirdparties/publicsuffix.org/list/effective_tld_names.dat
Provides:       bundled(publicsuffix-list) = 20220330

%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and
enforce thousands more filters than other popular blockers out there.

Flexible, it's more than an "ad blocker": it can also read and create filters
from hosts files.

%prep
# https://github.com/gorhill/uBlock/tree/master/dist#build-instructions-for-developers
%setup -q -n uBlock-%{version}
tar -xz -C submodules/uAssets --strip-components=1 -f %{SOURCE2}
%patch0 -p1
rm src/{js/wasm,lib/{lz4,publicsuffixlist/wasm}}/*.wasm
mv src/css/fonts/Inter/LICENSE.txt LICENSE.Inter.txt
mv src/img/fontawesome/LICENSE.txt LICENSE.fontawesome.txt
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
%license LICENSE.Inter.txt
%license src/css/fonts/Metropolis/UNLICENSE
%{firefox_inst_dir}/%{ext_id}.xpi
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Tue Oct 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.44.4-1
- update to 1.44.4 (#2118741)
- drop obsolete patch

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.43.0-1
- update to 1.43.0 (#2095350)

* Sun May 22 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.42.4-1
- update to 1.42.4 (#2070185)
- new bundled library: hsluv
- fix build with wabt 1.0.25+

* Fri Mar 11 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.41.8-1
- update to 1.41.8 (#2055291)

* Tue Feb 15 2022 Dominik Mierzejewski <rpm@greysector.net> - 1.41.2-1
- update to 1.41.2 (#2052004)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Dominik Mierzejewski <rpm@greysector.net> - 1.40.8-1
- update to 1.40.8 (#2034966)

* Sat Dec 04 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.39.2-1
- update to 1.39.2 (#2025622)

* Fri Oct 15 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.38.6-1
- update to 1.38.6 (#2009380)

* Tue Sep 21 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.38.0-1
- update to 1.38.0 (#2005514)
- drop obsolete patch

* Wed Jul 28 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.37.2-1
- update to 1.37.2 (#1986999)

* Sat Jul 24 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.37.0-1
- update to 1.37.0 (#1985343)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.36.2-1
- update to 1.36.2 (#1979628)

* Mon Jul 05 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.36.0-1
- update to 1.36.0 (#1974010)
- update declared version of bundled publicsuffix-list

* Tue Jun 08 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.35.2-1
- update to 1.35.2 (#1954349)

* Fri Apr 23 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.35.0-1
- update to 1.35.0 (#1946869)

* Thu Apr 01 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.34.0-1
- update to 1.34.0 (#1925264)

* Tue Feb 02 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.33.2-1
- update to 1.33.2 (#1922482)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.32.4-1
- update to 1.32.4 (#1918447)

* Thu Aug 20 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.29.0-1
- update to 1.29.0 (#1867396)
- optimize lz4 wasm code per upstream docs

* Thu Aug 06 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.28.4-2
- fix invalid JSON after Patch0 (caught by Raymond Hill)

* Wed Aug 05 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.28.4-1
- update to 1.28.4 (#1857445)
- avoid building on big-endian, wabt doesn't work there

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.28.2-3
- add missing explicit BR on python3

* Mon Jul 13 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.28.2-2
- use python3 in build script explicitly

* Sun Jul 12 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.28.2-1
- update to 1.28.2 (#1835275)
- "build" from upstream "source" directly
- drop non-free components from upstream uAssets tarball

* Sun May 03 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.26.2-1
- update to 1.26.2 (#1825039)

* Sun Apr 12 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.26.0-1
- update to 1.26.0 (#1820622)

* Sat Mar 14 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.25.2-1
- update to 1.25.2 (#1797341)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.24.2-1
- update to 1.24.2 (#1763778)

* Sat Sep 28 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.22.4-1
- update to 1.22.4 (#1756060)

* Wed Sep 11 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.22.2-2
- fix wrong fileid (was pointing to 1.20.0 instead of 1.22.2)

* Mon Sep 09 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.22.2-1
- update to 1.22.2 (#1713383)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.19.2-1
- update to 1.19.2 (#1689200)

* Thu Mar 14 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.18.6-1
- update to 1.18.6 (#1680421)
- drop conditionals that are true in F26+

* Wed Feb 20 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.18.4-1
- update to 1.18.4 (#1669295)
- update bundled fontawesome version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.17.2-1
- update to 1.17.2

* Mon Jul 30 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.16.14-1
- update to 1.16.14 (#1598265)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.16.12-1
- update to 1.16.12 (#1567576)

* Wed May 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.16.6-1
- update to 1.16.6 (#1567576)
- update bundled codemirror version

* Fri Apr 13 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.15.24-1
- update to 1.15.24
- use correct path for metainfo file
- update bundled components list and license tag
- include license texts in the standard location, too

* Tue Feb 20 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.15.10-1
- update to 1.15.10

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.14.24-1
- update to 1.14.24

* Fri Dec 29 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.14.22-1
- update to 1.14.22
- install the appdata metainfo file into correct place

* Wed Nov 29 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.14.18-1
- Initial package
