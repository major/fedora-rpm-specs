%global sheets_commit 0703cacbaf0dfc5cd31881bad48865fd836d70ca
%global sheets_commit_short 0703cac

# https://github.com/cheat/cheat
%global goipath         github.com/cheat/cheat
Version:                4.2.2
%global tag             4.2.2

%gometa

%global common_description %{expand:
Cheat allows you to create and view interactive cheatsheets on the command-
line. It was designed to help remind *nix system administrators of options for
commands that they use frequently, but not frequently enough to remember.}

%global golicenses      LICENSE.txt
%global godocs          README.md CONTRIBUTING.md cmd/cheat/docopt.txt

Name:           cheat
Release:        8%{?dist}
Summary:        Help for various commands and their use cases

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://github.com/cheat/cheatsheets/archive/%{sheets_commit_short}.tar.gz#/cheatsheets.tar.gz
Source2:        cheat-config-FEDORA.yml

BuildRequires:  golang(github.com/alecthomas/chroma/quick)
BuildRequires:  golang(github.com/docopt/docopt-go)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mgutz/ansi)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(gopkg.in/yaml.v1)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)

Recommends:     cheat-community-cheatsheets

%description
%{common_description}

# We wont use full versioned dependency because rpmdiff then complains about
# difference between noarch subpackages on different architectures
%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: bash bash-completion

%description bash-completion
Files needed to support bash completion.

%package fish-completion
Summary: Fish completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: fish

%description fish-completion
Files needed to support fish completion.

%package zsh-completion
Summary: Zsh completion support for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: zsh

%description zsh-completion
Files needed to support zsh completion.

%package community-cheatsheets
Summary:   Cheatsheets created by comunity for %{name}
URL:       https://github.com/cheat/cheatsheets
License:   CC0
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Supplements:  cheat

%description community-cheatsheets
Cheatsheets for various programs created and maintained by the
community.

%gopkg

%prep
%goprep
tar -xf %{SOURCE1}

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
mkdir -m 0755 -p                            %{buildroot}%{_datadir}/bash-completion/completions
mkdir -m 0755 -p                            %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -m 0755 -p                            %{buildroot}%{_datadir}/zsh/site-functions/

install -m 0644 -p scripts/cheat.bash %{buildroot}%{_datadir}/bash-completion/completions/cheat
install -m 0644 -p scripts/cheat.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/cheat.fish
install -m 0644 -p scripts/cheat.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_cheat

install -m 0755 -vd                         %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/cheat %{buildroot}%{_bindir}/

# Install cheatsheets
mkdir -m 0755 -p %{buildroot}/%{_datadir}/cheat

for sheet in cheatsheets-%{sheets_commit}/* ; do
  install -m 0644 -p $sheet %{buildroot}/%{_datadir}/cheat/
done

mkdir -m 0755 -p %{buildroot}%{_sysconfdir}/cheat
install -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/cheat/conf.yml

%check
%gocheck

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md cmd/cheat/docopt.txt
%config(noreplace) %{_sysconfdir}/cheat/conf.yml
%{_bindir}/cheat

%files community-cheatsheets
%license cheatsheets-%{sheets_commit}/.github/LICENSE.txt
%{_datadir}/cheat/

%files bash-completion
%{_datadir}/bash-completion/completions/cheat

%files fish-completion
%{_datadir}/fish/vendor_completions.d/cheat.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_cheat

%gopkgfiles

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 4.2.2-5
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.2.2-4
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Tomas Korbar <tkorbar@redhat.com> - 4.2.2-1
- Rebase to 4.2.2
- Resolves: rhbz#1955026

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Tomas Korbar <tkorbar@redhat.com> - 4.2.0-1
- Update to 4.2.0

* Thu Nov 19 2020 Tomas Korbar <tkorbar@redhat.com> - 4.1.1-1
- Update to 4.1.1

* Mon Aug 31 2020 Tomas Korbar <tkorbar@redhat.com> - 4.0.4-1
- Update to 4.0.4

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tomas Korbar <tkorbar@redhat.com> - 4.0.2-1
- Update to 4.0.2

* Thu Jan 30 2020 Tomas Korbar <tkorbar@redhat.com> - 3.6.0-1
- Rebase cheat to version 3.6.0 (#1793381)
- Rebase cheatsheets to commit 18c9374

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Tomas Korbar <tkorbar@redhat.com> - 3.2.2-1
- Rebase cheat to version 3.2.2 (#1786883)

* Mon Dec 16 2019 Tomas Korbar <tkorbar@redhat.com> - 3.2.1-1
- Rebase cheat to version 3.2.1 (#1771683)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Tomas Korbar <tkorbar@redhat.com> - 2.5.1-3
- Fix typo in fish completions folder
- Related: 1716145

* Wed Jun 12 2019 Tomas Korbar <tkorbar@redhat.com> - 2.5.1-2
- 1716145 - Package autocompletion files for cheat

* Wed Feb 20 2019 Tomas Korbar <tkorbar@redhat.com> - 2.5.1-1
- Specfile changed accordingly to review

* Mon Jan 28 2019 Tomas Korbar tkorbar@redhat.com - 2.5.1-1
- Initial commit of package
