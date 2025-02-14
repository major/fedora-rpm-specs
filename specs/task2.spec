# compat package for taskwarrior v2
# https://fedoraproject.org/wiki/Changes/Taskwarrior3

%global upstream_name task

Name:           task2
Version:        2.6.2
Release:        %autorelease
Summary:        Taskwarrior - a command-line TODO list manager
License:        MIT
URL:            https://taskwarrior.org
Source0:        %{url}/download/%{upstream_name}-%{version}.tar.gz

Provides:       task = %{version}-%{release}
Obsoletes:      task < 3

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

This package provides the taskv2 compatibility package.


%prep
%autosetup -n %{upstream_name}-%{version}

# add #include <cstdint>
sed -i '/<Pig.h>/ a #include <cstdint>' src/libshared/src/JSON.h
grep -C4 -nri "<cstdint>" src/libshared/src/JSON.h

%build
%cmake -DTASK_RCDIR=share/%{upstream_name}
%cmake_build

%install
%cmake_install

# Move shell completion stuff to the right place
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm0644 scripts/zsh/_%{upstream_name} %{buildroot}%{_datadir}/zsh/site-functions/_%{upstream_name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm0644 scripts/bash/%{upstream_name}.sh %{buildroot}%{_datadir}/bash-completion/completions/%{upstream_name}
mkdir -p %{buildroot}%{_datadir}/fish/completions/
install -Dpm0644 scripts/fish/%{upstream_name}.fish %{buildroot}%{_datadir}/fish/completions/%{upstream_name}.fish

# Fix perms and drop shebangs
# that's only docs and it's written in README about permissings
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'

rm -vrf %{buildroot}%{_datadir}/doc/%{upstream_name}/

%files
%license LICENSE
%doc NEWS doc/ref/%{upstream_name}-ref.pdf
%doc scripts/vim/ scripts/hooks/
%{_bindir}/%{upstream_name}
# We don't want to have refresh script there
%exclude %{_datadir}/%{upstream_name}/refresh
%{_datadir}/%{upstream_name}/
%{_mandir}/man1/%{upstream_name}.1*
%{_mandir}/man5/%{upstream_name}rc.5*
%{_mandir}/man5/%{upstream_name}-color.5*
%{_mandir}/man5/%{upstream_name}-sync.5*
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{upstream_name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{upstream_name}
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/completions/
%{_datadir}/fish/completions/%{upstream_name}.fish

%changelog
%autochangelog
