# FIXME: Patch to fix for increased safety
%global build_type_safety_c 0

%global commit 49457116bb0796636fd1bc84f39006fb102bfafc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20161025

Name:           glimpse
Version:        4.12.6^git%{commitdate}.%{shortcommit}
Release:        5%{?dist}
Summary:        Powerful file indexing and query system

License:        ISC
URL:            https://github.com/gvelez17/glimpse
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# From Debian
Patch0:         fix-makefile.patch
Patch1:         fix-makefile-cc-var.patch
Patch2:         agrep-fix-double-free.patch

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gcc
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  flex-devel
%else
BuildRequires:  libfl-static
%endif
BuildRequires:  make
Requires:       agrep

%description
Glimpse is a very powerful indexing and query system that allows you to
search through all your files very quickly.  It can be used by
individuals for their personal file systems as well as by organizations
for large data collections.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
autoconf
%configure
# Parallel make breaks it
make DEBUGFLAGS="%{build_cflags}" OTHERLIBS="%{build_ldflags}"


%install
make install prefix="%{buildroot}%{_prefix}" exec_prefix="%{buildroot}%{_prefix}" manprefix="%{buildroot}%{_mandir}"

# Move undocumented commands to libexec
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/*cast %{buildroot}%{_bindir}/tbuild %{buildroot}%{_bindir}/wgconvert %{buildroot}%{_libexecdir}/%{name}

# Drop agrep, as we have another provider for it
rm -v %{buildroot}%{_bindir}/agrep %{buildroot}%{_mandir}/man1/agrep.1*


%files
%license LICENSE
%doc README KNOWN_BUGS ChangeLog CHANGES
%{_bindir}/glimpse*
%{_mandir}/man1/glimpse*
%{_libexecdir}/glimpse/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.6^git20161025.4945711-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.6^git20161025.4945711-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.6^git20161025.4945711-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.6^git20161025.4945711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 4.12.6^git20161025.4945711-1
- Initial package
