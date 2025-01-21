Name:           toga2
Version:        4.0
Release:        10%{?dist}
Summary:        UCI chess engine based on Fruit

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66174
Source0:        https://www.mediafire.com/file/4c8m5lejoo7fi3d/TogaII40.zip
# This manpage comes from the toga2-3.0.0.1SE1-2 Debian package
Source1:        toga2.6

BuildRequires:  gcc-c++
BuildRequires:  sed

%description
Toga II is a UCI chess engine based on Fruit.

%prep
%setup -q -n TogaII40
# Remove precompiled binaries
rm -r Windows
# Convert readme to UTF-8 and Unix end-of-line encodings
f=readme.txt
iconv --from=ISO-8859-1 --to=UTF-8 "${f}" > "${f}.utf8"
touch -r "${f}" "${f}.utf8"
mv "${f}.utf8" "${f}"
sed -i 's/\r$//' "${f}"

%build
pushd src
%{__cxx} -o toga2 %{optflags} *.cpp %{build_ldflags} -lm -lpthread

%install
mkdir -p %{buildroot}/%{_bindir}
cp -P src/toga2 %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man6
cp -P %SOURCE1 %{buildroot}/%{_mandir}/man6

%files
%license copying.txt
%doc readme.txt
%{_bindir}/toga2
%{_mandir}/man6/%{name}.6*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0-9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 4.0-1
- Initial package
