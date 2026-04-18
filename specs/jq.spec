%bcond check 1

Name:           jq
Version:        1.8.1
Release:        %autorelease
Summary:        Command-line JSON processor

License:        MIT AND ICU AND CC-BY-3.0
URL:            https://jqlang.org/
Source0:        https://github.com/jqlang/jq/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  oniguruma-devel

%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  make
BuildRequires:  tzdata

# Fix <skipped: too deep> error
# https://github.com/jqlang/jq/issues/3413
# Somewhat of a precursor to fix for CVE-2026-33947
Patch:          skipped_too_deep.patch
# https://github.com/jqlang/jq/security/advisories/GHSA-q3h9-m34w-h76f
Patch:          CVE-2026-32316.patch
# https://github.com/jqlang/jq/security/advisories/GHSA-6gc3-3g9p-xx28
Patch:          CVE-2026-39956.patch
# https://github.com/jqlang/jq/security/advisories/GHSA-2hhh-px8h-355p
Patch:          CVE-2026-39979.patch
# https://github.com/jqlang/jq/security/advisories/GHSA-wwj8-gxm6-jc29
Patch:          CVE-2026-40164.patch
# https://github.com/jqlang/jq/security/advisories/GHSA-6gc3-3g9p-xx28
Patch:          CVE-2026-33947.patch

%description
lightweight and flexible command-line JSON processor

 jq is like sed for JSON data – you can use it to slice
 and filter and map and transform structured data with
 the same ease that sed, awk, grep and friends let you
 play with text.

 It is written in portable C, and it has zero runtime
 dependencies.

 jq can mangle the data format that you have into the
 one that you want with very little effort, and the
 program to do so is often shorter and simpler than
 you'd expect.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


%prep
%autosetup -p1

%build
%configure --disable-static
%make_build
# Docs already shipped in jq's tarball.
# In order to build the manual page, it
# is necessary to install rake, rubygem-ronn
# and do the following steps:
#
# # yum install rake rubygem-ronn
# $ cd docs/
# $ curl -L https://get.rvm.io | bash -s stable --ruby=1.9.3
# $ source $HOME/.rvm/scripts/rvm
# $ bundle install
# $ cd ..
# $ ./configure
# $ make real_docs

%install
%make_install

%if %{with check}
%check
# Valgrind used, so restrict architectures for check
%ifarch x86_64
make check
%endif
%endif

%files
%license COPYING
%doc AUTHORS COPYING NEWS.md README.md
%{_bindir}/%{name}
%{_libdir}/libjq.so.*
%{_datadir}/man/man1/jq.1.gz

%files devel
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so
%{_libdir}/pkgconfig/libjq.pc

%changelog
%autochangelog
