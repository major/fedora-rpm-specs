%global _R_libdir_check %{nil}

Name:           R-littler
Version:        %R_rpm_version 0.3.21
Release:        %autorelease
Summary:        littler: R at the Command-Line via 'r'

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A scripting and command-line front-end is provided by 'r' (aka 'littler')
as a lightweight binary wrapper around the GNU R language and environment
for statistical computing and graphics. While R can be used in batch
mode, the r binary adds full support for both 'shebang'-style scripting
(i.e. using a hash-mark-exclamation-path expression as the first line in
scripts) as well as command-line use in standard Unix pipelines. In other
words, r provides the R language without the environment.

%package examples
Summary:        R-littler Examples
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
Examples for using R-littler.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
rm -rf %{buildroot}%{_R_libdir}/littler/script-tests

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_R_libdir}/littler/bin/r \
   %{buildroot}%{_bindir}
rmdir %{buildroot}%{_R_libdir}/littler/bin
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_R_libdir}/littler/man-page/r.1 \
   %{buildroot}%{_mandir}/man1
rmdir %{buildroot}%{_R_libdir}/littler/man-page

for f in %{buildroot}%{_R_libdir}/littler/examples/* ; do
    grep -q '/usr/bin/env r' $f && sed 's!/usr/bin/env r!/usr/bin/r!' -i $f
done

%R_save_files
grep -v examples %{R_files} > %{R_files}.main
grep examples %{R_files} > %{R_files}.examples

%check
%R_check

%files -f %{R_files}.main
%{_bindir}/r
%{_mandir}/man1/r.1*

%files examples -f %{R_files}.examples

%changelog
%autochangelog
