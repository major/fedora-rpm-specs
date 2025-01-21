Version: 3.003
Release: 5%{dist}
URL: https://sourcefoundry.org/hack/

%global foundry           source-foundry
%global fontlicense       MIT AND Bitstream-Vera
%global fontlicenses      LICENSE.md
%global fontdocs          README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily Hack
%global fontsummary A typeface designed for source code

%global fonts             *.ttf
%global fontconfs         45-Hack.conf

%global fontdescription   %{expand:
Hack is designed to be a workhorse typeface for source code. It has deep roots
in the free, open source typeface community and expands upon the contributions
of the Bitstream Vera & DejaVu projects.
The large x-height + wide aperture + low contrast design make it legible at
commonly used source code text sizes with a sweet spot that runs in the
8 - 14 range.

Hack is a derivative of upstream Bitstream Vera Sans Mono and DejaVu Sans Mono
source. The Hack changes are licensed under the MIT license.
Bitstream Vera Sans Mono is licensed under the Bitstream Vera license and
maintains reserved font names "Bitstream" and "Vera". The DejaVu changes to
the Bitstream Vera source were committed to the public domain.
}

Source0: https://github.com/source-foundry/Hack/releases/download/v%{version}/Hack-v%{version}-ttf.tar.xz
Source1: https://github.com/source-foundry/Hack/raw/v%{version}/LICENSE.md
Source2: https://github.com/source-foundry/Hack/raw/v%{version}/README.md

# https://github.com/source-foundry/Hack/pull/644
# Use systemId urn:fontconfig:fonts.dtd to reference the fonts.dtd type defintion #644
Patch0: https://github.com/source-foundry/Hack/pull/644.patch

Source10: https://github.com/source-foundry/Hack/raw/v%{version}/config/fontconfig/45-Hack.conf

BuildRequires: fontconfig

%fontpkg

%prep
%setup -c
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE10} .
%patch -P0 -p3

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Nov 30 2022 Jonny Heggheim <hegjon@gmail.com> - 3.003-1
- Initial package
