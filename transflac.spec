%global forgeurl    https://bitbucket.org/gbcox/transflac/
%global commit      985d785b20891fb506bbfcb0b6bf186423c12f80

Name:           transflac
Version:        1.0.2
Summary:        Transcode FLAC to lossy formats
License:        GPLv3+

%{forgemeta}

URL:            %{forgeurl}
Release:        3%{?dist}
Source0:        %{forgesource}
Source1:        %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  make
Requires:       figlet
Requires:       flac
Requires:       vorbis-tools
Requires:       opus-tools
Requires:       rsync
Requires:       procps-ng
Requires:       coreutils

%description
transflac is a front end command line utility (actually, a bash script)
that transcodes FLAC audio files into various lossy formats.

%prep
%{forgesetup}
%autosetup -n %{archivename}

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}

%files
%license LICENSE.md
%doc README.md contributors.txt
%config(noreplace) %{_sysconfdir}/transflac.conf
%{_bindir}/transflac
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/src-tf-set-colors.sh
%{_libexecdir}/%{name}/src-tf-ck-codec.sh
%{_libexecdir}/%{name}/src-tf-ck-input.sh
%{_libexecdir}/%{name}/src-tf-ck-output.sh
%{_libexecdir}/%{name}/src-tf-ck-quality.sh
%{_libexecdir}/%{name}/src-tf-codec.sh
%{_libexecdir}/%{name}/src-tf-figlet.sh
%{_libexecdir}/%{name}/src-tf-help.sh
%{_libexecdir}/%{name}/src-tf-terminal-header.sh
%{_libexecdir}/%{name}/src-tf-table.sh
%{_libexecdir}/%{name}/src-tf-progress-bar.sh
%{_mandir}/man1/transflac.1*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.2-1
- Upstream release rhbz#2058360

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.1-1
- Upstream release rhbz#1767252

* Thu Oct 31 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-3
- Fedora Review rhbz#1767252

* Thu Oct 31 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-2
- Fedora Review rhbz#1767252

* Wed Oct 30 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-1
- initial build
