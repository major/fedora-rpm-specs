Name:           task
Version:        2.6.2
Release:        %autorelease
Summary:        Taskwarrior - a command-line TODO list manager
License:        MIT
URL:            https://taskwarrior.org
Source0:        %{url}/download/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  libuuid-devel
BuildRequires:  gnutls-devel

%description
Taskwarrior is a command-line TODO list manager. It is flexible, fast,
efficient, unobtrusive, does its job then gets out of your way.

Taskwarrior scales to fit your workflow. Use it as a simple app that captures
tasks, shows you the list, and removes tasks from that list. Leverage its
capabilities though, and it becomes a sophisticated data query tool that can
help you stay organized, and get through your work.

%prep
%autosetup

%build
%cmake -DTASK_RCDIR=share/%{name}
%cmake_build

%install
%cmake_install

# Move shell completion stuff to the right place
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm0644 scripts/zsh/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm0644 scripts/bash/%{name}.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/fish/completions/
install -Dpm0644 scripts/fish/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish

# Fix perms and drop shebangs
# that's only docs and it's written in README about permissings
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'

rm -vrf %{buildroot}%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc NEWS doc/ref/%{name}-ref.pdf
%doc scripts/vim/ scripts/hooks/
%{_bindir}/%{name}
# We don't want to have refresh script there
%exclude %{_datadir}/%{name}/refresh
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*
%{_mandir}/man5/%{name}-color.5*
%{_mandir}/man5/%{name}-sync.5*
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/completions/
%{_datadir}/fish/completions/%{name}.fish

%changelog
%autochangelog
