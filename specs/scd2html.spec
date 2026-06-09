Name:           scd2html
Version:        1.0.0
Release:        %autorelease
Summary:        Generates HTML for scdoc source files

License:        MIT
URL:            https://sr.ht/~bitfehler/scd2html
%global furl    https://git.sr.ht/~bitfehler/scd2html
Source:         %{furl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch:          https://git.sr.ht/~bitfehler/scd2html/commit/7fd6434fe74dc08cb8cbd15b9bfc374a87ec0d11.patch#/fix-compiler-warnings.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  re2c
# scdoc is used to build scd2html's manpage
BuildRequires:  scdoc


%description
scd2html generates HTML from scdoc source files


%prep
%autosetup -C -p1

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
%autochangelog
