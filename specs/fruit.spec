Name:           fruit
Version:        2.1
Release:        11%{?dist}
Summary:        UCI chess engine

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://arctrix.com/nas/chess/fruit
Source0:        %{url}/fruit_21_linux.zip
Source1:        https://web.archive.org/web/20080117060815/http://wbec-ridderkerk.nl/html/download/fruit/Dann_Books.zip
Source2:        https://salsa.debian.org/debian/fruit/-/raw/debian/master/debian/fruit.6

# Accept go command without arguments
Patch0:         https://salsa.debian.org/debian/fruit/-/raw/debian/master/debian/patches/02-simple_go.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

Recommends:     %{name}-books

%description
Fruit is a chess engine that uses the UCI protocol.

%package books
Summary:        Opening books for %{name}
BuildArch:      noarch
Requires:       fruit

%description books
This package includes opening books for the Fruit chess engine.

%prep
%autosetup -n fruit_21_linux -p1 -b 1
# Remove precompiled binary
rm fruit_21_static
# Convert docs to Unix end-of-line encodings
mv ../Dann_Books/Readme.txt .
sed -i 's/\r$//' readme.txt technical_10.txt Readme.txt
# Fix default opening book path
sed -i 's:book_small.bin:%{_datadir}/%{name}/book_small.bin:' src/option.cpp

%build
%make_build -C src \
  CXXFLAGS="%{optflags} -fstrict-aliasing" \
  LDFLAGS="%{build_ldflags} -lm"

%install
mkdir -p %{buildroot}/%{_bindir}
cp -P src/fruit %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -P book_small.bin %{buildroot}/%{_datadir}/%{name}
cp -PR ../Dann_Books %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_mandir}/man6
cp -P %SOURCE2 %{buildroot}/%{_mandir}/man6

%files
%license copying.txt
%doc readme.txt technical_10.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*

%files books
%license copying.txt
%doc Readme.txt
%{_datadir}/%{name}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 24 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.1-1
- Initial package
