%global extdir		%{_datadir}/gnome-shell/extensions/suspend-button@laserb
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/laserb/%{name}

%global commit		a81252074de99e2cdd29913b7f797a7f0d6d5b2b
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global commitdate	20171024
%global gitrel		.%{commitdate}git%{shortcommit}
%global gitver		-%{commitdate}git%{shortcommit}


Name:		gnome-shell-extension-suspend-button
Version:	19
Release:	18%{?gitrel}%{?dist}
Summary:	GNOME Shell Extension Suspend-Button by laserb

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://extensions.gnome.org/extension/826/suspend-button/
Source0:	%{giturl}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitversion}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas
BuildRequires: make

Requires:	gnome-shell-extension-common

%description
Allows to modify the suspend/shutdown button in the status menu.


%prep
%autosetup -n %{name}-%{commit} -p 1


%build
%make_build


%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install schema.
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr _build/schemas/*gschema.xml %{buildroot}%{gschemadir}

# Install i18n.
%{_bindir}/find _build -name '*.po' -print -delete
%{__cp} -pr _build/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name


# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
	%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi


%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19-18.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 19-17.20171024gita812520
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-16.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-15.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-14.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-13.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-12.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-11.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-10.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-9.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-8.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-7.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-6.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-5.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-4.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-3.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-2.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 19-1.20171024gita812520
- Initial import (rhbz#1520152)

* Fri Dec 01 2017 Björn Esser <besser82@fedoraproject.org> - 19-0.1.20171024gita812520
- Initial rpm release (rhbz#1520152)
