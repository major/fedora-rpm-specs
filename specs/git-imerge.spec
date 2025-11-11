Name:           git-imerge
Version:        1.2.0
Release:        %autorelease
Summary:        Incremental merge and rebase for Git
License:        GPL-2.0-or-later
URL:            https://github.com/mhagger/git-imerge
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  git-core
BuildRequires:  python3-devel

Requires:       git-core

%description
Performs a merge between two branches incrementally. If conflicts are
encountered, figures out exactly which pairs of commits conflict, and presents
the user with one pairwise conflict at a time for resolution.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gitimerge
# Move the Bash completion file to its correct location
mv "%{buildroot}%{python3_sitelib}%{_datadir}" "%{buildroot}%{_prefix}/"


%check
%tox


%files -f %{pyproject_files}
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}


%changelog
%autochangelog
