# Test dependencies too old for RHEL 10
%if 0%{?rhel}
%bcond tests 0
%else
%bcond tests 1
%endif

Name: pulp-cli
Version: 0.37.0
Release: %autorelease
Summary: Command line interface to talk to the Pulp 3 REST API
License: GPL-2.0-or-later
URL: https://github.com/pulp/%{name}
BuildArch: noarch

Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel

Recommends: pulp-cli-deb
Recommends: python3-pygments
Recommends: python3-click-shell
Recommends: python3-secretstorage

%description
%{name} provides the "pulp" command, able to communicate with the Pulp3 API in
a more natural way than plain http. Specifically, resources can not only be
referenced by their href, but also their natural key (e.g. name). It also
handles waiting on tasks on behalf of the user.


%prep
%autosetup -p1

# Remove the Python version upper bound to enable building with new versions in Fedora
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

# Remove all bounds on test dependencies; we must use what we have
sed -r -Ei 's/^([a-zA-Z0-9._-]+).*/\1/' test_requirements.txt

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires test_requirements.txt
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pulp_cli pulpcore pytest_pulp_cli

# Shell completion (borrowed from rpmautospec)
for shell_path in \
        bash:%{bash_completions_dir}/pulp \
        fish:%{fish_completions_dir}/pulp.fish \
        zsh:%{zsh_completions_dir}/_pulp; do
    shell="${shell_path%%:*}"
    path="${shell_path#*:}"
    dir="${path%/*}"

    install -m 755 -d "%{buildroot}${dir}"

    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _PULP_COMPLETE="${shell}_source" \
    %{__python3} -c \
    "import sys; sys.argv = ['pulp']; from pulp_cli import main; sys.exit(main())" \
    > "%{buildroot}${path}"
done


%if %{with tests}
%check
%pyproject_check_import pulp_cli
%pytest -m help_page
%endif


%files -f %{pyproject_files}
%license LICENSE
%doc README.*
%{_bindir}/pulp
%dir %{bash_completions_dir}
%{bash_completions_dir}/pulp
%dir %{fish_completions_dir}
%{fish_completions_dir}/pulp.fish
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_pulp


%changelog
%autochangelog
