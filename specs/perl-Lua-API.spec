Name:           perl-Lua-API
Version:        0.04
Release:        9%{?dist}
Summary:        Interface to Lua's embedding API
License:        GPL-3.0-or-later

URL:            https://metacpan.org/release/Lua-API
Source0:        http://www.cpan.org/authors/id/D/DJ/DJERIUS/Lua-API-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(XSLoader) >= 0.1
BuildRequires:  pkgconfig
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  pkgconfig(lua) < 5.2
%else
BuildRequires:  pkgconfig(lua-5.1)
%endif

Requires:       perl(XSLoader) >= 0.1

%description
Lua is a simple, expressive, extension programming language that is easily
embeddable. Lua::API provides Perl bindings to Lua's C-based embedding
API. It allows Perl routines to be called from Lua as if they were written
in C, and allows Perl routines to directly manipulate the Lua interpreter
and its environment. It presents a very low-level interface (essentially
equivalent to the C interface), so is aimed at developers who need that
sort of access.

%prep
%autosetup -n Lua-API-%{version}

%build
%if 0%{?rhel} && 0%{?rhel} <= 7
export LUA_INC=$(pkg-config --cflags lua)
export LUA_LIBS=$(pkg-config --libs lua)
%else
export LUA_INC=$(pkg-config --cflags lua-5.1)
export LUA_LIBS=$(pkg-config --libs lua-5.1)
%endif
PERL_USE_UNSAFE_INC=1 %{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

# Fix weird permissions (555) on shared object file
chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Lua/API/API.so

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%check
make test

%files
%doc ChangeLog Changes README
%license LICENSE
%{perl_vendorarch}/auto/Lua/
%{perl_vendorarch}/Lua/
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-7
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-3
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 14 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.04-1
- Initial package
