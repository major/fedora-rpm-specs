%global commit      4f62aae8abfa5175e0a9bd083e4f815bb6ff7a06
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191019

Name:           gedit-color-schemes
Version:        0
Release:        17.%{date}git%{shortcommit}%{?dist}
Summary:        Color schemes for Gedit and apps to render the syntax highlight

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/trusktr/gedit-color-schemes
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  libappstream-glib
Requires:       gtksourceview3
Requires:       gtksourceview4
Recommends:     gedit
Suggests:       %{name}-gtksourceview-2

%description
These are syntax highlight text color schemes for Gedit (or apps that use
GtkSourceView).


%package        gtksourceview-2
Summary:        gtksourceview-2.0 schemes for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gtksourceview2

%description    gtksourceview-2
gtksourceview-2.0 schemes for %{name}.


%prep
%autosetup -n %{name}-%{commit} -p1
rm gtksourceview-*.0/styles/install.sh

### To prevent conflicts with 'gtksourceview2' package
rm gtksourceview-2.0/styles/cobalt.xml
rm gtksourceview-2.0/styles/oblivion.xml

### To prevent conflicts with 'gtksourceview3' package
rm gtksourceview-3.0/styles/solarized-*


%install
mkdir -p                        %{buildroot}%{_datadir}/gtksourceview-2.0
cp -a gtksourceview-2.0/styles  %{buildroot}%{_datadir}/gtksourceview-2.0/

mkdir -p                        %{buildroot}%{_datadir}/gtksourceview-3.0
cp -a gtksourceview-3.0/styles  %{buildroot}%{_datadir}/gtksourceview-3.0/

mkdir -p                        %{buildroot}%{_datadir}/gtksourceview-4
cp -a gtksourceview-3.0/styles  %{buildroot}%{_datadir}/gtksourceview-4/

%fdupes -s %{buildroot}%{_datadir}/gtksourceview-*

install -m 0644 -Dp %{SOURCE1}  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc README.md
%{_datadir}/gtksourceview-3.0/
%{_datadir}/gtksourceview-4/
%{_metainfodir}/*.xml

%files gtksourceview-2
%{_datadir}/gtksourceview-2.0/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-16.20191019git4f62aae
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20191019git4f62aae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20191019git4f62aae
- Packaging fixes

* Sat Oct 19 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20130722git4f62aae
- Initial package
