%define debug_package %{nil}

Name:           bacula-docs
Version:        9.6.7
Release:        7%{?dist}
Summary:        Bacula documentation
License:        AGPLv3 with exceptions
URL:            http://www.bacula.org

Source0:        http://downloads.sourceforge.net/bacula/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  ghostscript
BuildRequires:  inkscape
BuildRequires:  latex2html
BuildRequires:  make
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  tex(babel.sty)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(setspace.sty)

Provides:       bacula-docs = %{version}-%{release}
Obsoletes:      bacula-docs < 5.2.2-4

%description
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the documentation for most of the Bacula packages.

%prep
%autosetup -p1

%build
make

mkdir result
for manual in console developers main misc problems utility; do
    mkdir result/$manual
    cp -f manuals/en/pdf-and-html/$manual/*.html result/$manual
    cp -f manuals/en/pdf-and-html/$manual/*.pdf result/.
done
cp -fra manuals/en/pdf-and-html/images result/.

%install

%files
%license LICENSE LICENSE-FOSS
%doc result/*

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Simone Caronni <negativo17@gmail.com> - 9.6.7-1
- Update to 9.6.7.
- Trim changelog.
- Remove RHEL/CentOS 6 build support.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Simone Caronni <negativo17@gmail.com> - 9.4.1-1
- Update to 9.4.1.

* Tue Aug 21 2018 Simone Caronni <negativo17@gmail.com> - 9.2.1-1
- Update to 9.2.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Simone Caronni <negativo17@gmail.com> - 9.0.8-1
- Update to 9.0.8.

* Mon May 14 2018 Simone Caronni <negativo17@gmail.com> - 9.0.7-1
- Update to 9.0.7.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
