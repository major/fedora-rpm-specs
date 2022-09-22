Name:           tldr
Version:        3.1.0
Release:        %autorelease
Summary:        Simplified and community-driven man pages

License:        MIT
URL:            https://github.com/tldr-pages/tldr-python-client
Source0:        https://github.com/tldr-pages/tldr-python-client/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  make
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(shtab)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-argparse)
BuildRequires:  python3dist(termcolor)
# dependencies for %%check
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)


%description
A Python command line client for tldr - Simplified and community-driven
man pages http://tldr-pages.github.io/.

%prep
%autosetup -n %{name}-python-client-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
pushd docs
make man
popd
%pyproject_wheel
%{python3} tldr.py --print-completion bash > tldr.bash
%{python3} tldr.py --print-completion zsh > tldr.zsh

%install
%pyproject_install
%pyproject_save_files tldr

install -Dp --mode=0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp --mode=0644 %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}


%check
%pytest -k "not test_error_message"

%files -f %{pyproject_files}
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/tldr.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
%autochangelog
