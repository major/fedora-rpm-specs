#global commit		2394e7f7180542beccaad28cb557045ff07ecd48
#global shortcommit	%(c=%{commit}; echo ${c:0:7})
#global gitdate	20220331
#global fgittag	%{gitdate}.git%{shortcommit}
%global extdir		caffeine@patapon.info
%global gschemadir	%{_datadir}/glib-2.0/schemas

Name:		gnome-shell-extension-caffeine
Version:	48
Release:	1%{?fgittag:.%{fgittag}}%{?dist}
Summary:	Disable the screen saver and auto suspend in gnome shell

License:	GPLv2
URL:		https://github.com/eonpatapon/gnome-shell-extension-caffeine
%if 0%{?shortcommit:1}
Source0:	https://github.com/eonpatapon/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/eonpatapon/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
%endif

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas

Requires:	gnome-shell-extension-common

%description
This extension allows the user to easily disable the screen saver and auto
suspend in gnome shell via an icon in the top bar. By default, this function
is also enabled if a full screen application is running, and can be configured
to disable gnome shell's night light as well.

%prep
%autosetup %{?commit:-n %{name}-%{commit}}

%build
./update-locale.sh
glib-compile-schemas --strict --targetdir=%{extdir}/schemas/ %{extdir}/schemas

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -ar %{extdir} %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}
%find_lang %{name} --all-name

# Fedora and EPEL 8 handles post scripts via triggers
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
%{_datadir}/gnome-shell/extensions/%{extdir}

%changelog
* Fri May 05 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 48-1
- Update to v48

* Fri Apr 21 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 47-1
- Update to v47

* Fri Mar 17 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 46-1
- Update to v46

* Wed Feb 08 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 44-1
- Update to v44

* Mon Jan 30 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 43-1
- Update to v43

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 15 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 42-1
- Update to v42

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-4.20220331.git2394e7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 39-3.20220331.git2394e7f
- Update to git snapshot to fix f36

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 39-1
- Update to v39

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 38-1
- Update to v38

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 37-1
- Initial package
