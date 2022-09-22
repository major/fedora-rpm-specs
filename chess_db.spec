%bcond_without tests

%global forgeurl https://github.com/pychess/chess_db
%global commit eb41ddf4cb5eb6ef5eedaa4d9006f4d2e8a60dd6
%forgemeta

Name:           chess_db
Version:        0.2
Release:        4%{?dist}
Summary:        Chess database opening tree indexer

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  sed
%if %{with tests}
BuildRequires:  python3dist(pexpect)
%endif

%description
This project helps index PGN files to polyglot books with the standard moves
and weights, but also has Win/Loss/Draw Stats and game_index information.

%prep
%forgesetup
# Fix python shebang
sed -e 's:/usr/bin/env python:/usr/bin/python3:' -i parser/*.py
# Drop arch bitness flags as they break the build on ARM
sed -e 's:-m$(bits)::g' -i parser/Makefile

%build
pushd parser
%make_build build \
  ARCH="general-%{__isa_bits}" \
  EXTRACXXFLAGS="%{optflags}" \
  EXTRALDFLAGS="${build_ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 parser/parser %{buildroot}%{_bindir}/

%if %{with tests}
%check
pushd parser
%python3 test.py
%endif

%files
%license Copying.txt
%doc README.md parser/chess_db.py
%{_bindir}/parser

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May  9 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2-1.20210509giteb41ddf
- Initial package
