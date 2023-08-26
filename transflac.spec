%global forgeurl    https://bitbucket.org/gbcox/transflac/
%global commit      ff091c18ac0e

Name:           transflac
Version:        1.2.4
Summary:        Transcode FLAC to lossy formats
License:        GPL-3.0-or-later

%{forgemeta}

URL:            %{forgeurl}
Release:        %autorelease
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
Requires:       (ffmpeg or ffmpeg-free)

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
%{_libexecdir}/%{name}/src-tf-conf-override.sh
%{_libexecdir}/%{name}/src-tf-set-variables.sh
%{_libexecdir}/%{name}/src-tf-table.sh
%{_libexecdir}/%{name}/src-tf-progress-bar.sh
%{_mandir}/man1/transflac.1*

%changelog
%autochangelog
