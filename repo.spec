Name:           repo
Version:        2.45
Release:        %autorelease
Summary:        Repository management tool built on top of git

License:        Apache-2.0
URL:            https://gerrit.googlesource.com/git-repo
Source0:        %{url}/+archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  tree

Requires:       git
Requires:       gnupg2

%description
Repo is a tool built on top of Git. Repo helps manage many Git repositories,
does the uploads to revision control systems, and automates parts of the
development workflow. Repo is not meant to replace Git, only to make it easier
to work with Git.

%prep
%autosetup -c %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
# repo is an unusual tool because it downloads all of its own Python modules
# at runtime using GPG-signed git tags, and stores those files as part of the
# project that it is working with. This package just provides the wrapper
# script, which provides the GPG signing keys for verifying that the correct
# Python code was downloaded, so there's nothing to actually build.

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/%{name}*.1
install -Dpm0644 completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%check
%{py3_test_envvars} %{python3} -c 'import pytest; pytest.main()'

%files
%license LICENSE
%doc README.md docs/*.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
