Name:           scd2html
Version:        1.0.0
Release:        5%{?dist}
Summary:        Generates HTML for scdoc source files

License:        MIT
URL:            https://sr.ht/~bitfehler/scd2html
%global furl    https://git.sr.ht/~bitfehler/scd2html
Source:         %{furl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  re2c
# scdoc is used to build scd2html's manpage
BuildRequires:  scdoc


%description
scd2html generates HTML from scdoc source files


%prep
%autosetup -n scd2html-v%{version}

# Regenerate linkify.c from linkify.re
rm src/linkify.c

# Preserve mtimes and don't build a static binary
sed -i Makefile \
    -e 's|-static||' \
    -e 's|install -m|install -pm|'


%build
%make_build PREFIX=%{_prefix}
./scd2html <scd2html.1.scd >scd2html.1.html


%install
%make_install PREFIX=%{_prefix}


%files
%license COPYING
%doc README.md scd2html.1.html
%{_bindir}/scd2html
%{_mandir}/man1/scd2html.1*
%{_datadir}/pkgconfig/scd2html.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Dec 15 2022 Maxwell G <gotmax@e.email> - 1.0.0-1
- Initial package (rhbz#2169097).
