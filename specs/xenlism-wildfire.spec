%global gitdate 20160511
%global commit0 d3b9ad212f14b862e9473126062c5eaf25bd9f55

%global srcname wildfire
%global project xenlism

Name:           %{project}-%{srcname}
Version:        0
Release:        0.19.%{gitdate}git%(c=%{commit0}; echo ${c:0:7} )%{?dist}
Summary:        Minimalist theme for your desktop

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://%{project}.github.io/%{srcname}
Source0:        https://github.com/%{project}/%{srcname}/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildArch:      noarch
BuildRequires:  coreutils

%if 0%{?fedora}
Suggests:       %{name}-backgrounds = %{version}-%{release}
%endif

%description
Xenlism Wildfire is a desktop theme collection based on
vector graphics (svg,ai). Goals are minimalism and realism.


%package day
Summary:     Day theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description day
%{summary}.


%package night
Summary:     Night theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description night
%{summary}.


%package midnight
Summary:     Midnight theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description midnight
%{summary}.


%package monday
Summary:     Monday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description monday
%{summary}.

%package tuesday
Summary:     Tuesday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description tuesday
%{summary}.

%package wednesday
Summary:     Wednesday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description wednesday
%{summary}.

%package thursday
Summary:     Thursday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description thursday
%{summary}.

%package friday
Summary:     Friday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description friday
%{summary}.

%package saturday
Summary:     Saturday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description saturday
%{summary}.

%package sunday
Summary:     Sunday theme of Xenlism Wildfire
Requires:    %{name} = %{version}-%{release}

%description sunday
%{summary}.


%package backgrounds
Summary:     Backgrounds of Xenlism Wildfire
%if 0%{?fedora}
Enhances:    %{name} = %{version}-%{release}
%endif

%description backgrounds
%{summary}.


%prep
%setup -qn%{srcname}-%{commit0}
# W: hidden-file-or-dir, E: zero-length
find icons -name '.*' -print -delete
# W: spurious-executable-perm
#chmod -x Screenshot/*.png
# W: dangling-relative-symlink
rm icons/Xenlism-Wildfire/Mimes/text-x-lyx.svg

%build
# nothing

%install
# copied from upstream install script
install -dm755 %{buildroot}%{_datadir}
cp -pr icons %{buildroot}%{_datadir}
find  %{buildroot}%{_datadir}/icons -type d -exec chmod 755 '{}' \;
find  %{buildroot}%{_datadir}/icons -type f -exec chmod 644 '{}' \;
install -dm755 %{buildroot}%{_datadir}/backgrounds/xenlism
cp -pr wallpapers/* %{buildroot}%{_datadir}/backgrounds/%{project}
find %{buildroot}%{_datadir}/backgrounds/%{project} -type d -exec chmod 755 '{}' \;
find %{buildroot}%{_datadir}/backgrounds/%{project} -type f -exec chmod 644 '{}' \;
install -dm755 %{buildroot}%{_datadir}/gnome-background-properties
cp -pr background-properties/* %{buildroot}%{_datadir}/gnome-background-properties
find %{buildroot}%{_datadir}/gnome-background-properties -type d -exec chmod 755 '{}' \;
find %{buildroot}%{_datadir}/gnome-background-properties -type f -exec chmod 644 '{}' \;


%post
/bin/touch --no-create %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Xenlism-Wildfire* &>/dev/null || :


%files
%license LICENSE.md
%doc README.md
%{_datadir}/icons/Xenlism-Wildfire/

%files day
%{_datadir}/icons/Xenlism-Wildfire-Day/

%files night
%{_datadir}/icons/Xenlism-Wildfire-Night/

%files midnight
%{_datadir}/icons/Xenlism-Wildfire-MidNight/

%files monday
%{_datadir}/icons/Xenlism-Wildfire-MonDay/

%files tuesday
%{_datadir}/icons/Xenlism-Wildfire-TuesDay/

%files wednesday
%{_datadir}/icons/Xenlism-Wildfire-WednesDay/

%files thursday
%{_datadir}/icons/Xenlism-Wildfire-ThursDay/

%files friday
%{_datadir}/icons/Xenlism-Wildfire-FriDay/

%files saturday
%{_datadir}/icons/Xenlism-Wildfire-SaturDay/

%files sunday
%{_datadir}/icons/Xenlism-Wildfire-SunDay/

%files backgrounds
%license LICENSE.md
%doc README.md
#%%doc Screenshot/
%{_datadir}/backgrounds/%{project}/
%{_datadir}/gnome-background-properties/*.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.18.20160511gitd3b9ad2
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160511gitd3b9ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Raphael Groner <projects.rg@smart.ms> - 0-0.1.20160511gitd3b9ad2
- initial
