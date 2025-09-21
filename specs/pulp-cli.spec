Name: pulp-cli
Version: 0.36.0
Release: 2%{?dist}
Summary: Command line interface to talk to the Pulp 3 REST API

License: GPL-2.0-or-later
URL: https://github.com/pulp/pulp-cli
Source: %{url}/archive/%{version}/pulp-cli-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
Recommends: python3-pygments
Recommends: python3-click-shell
Recommends: python3-secretstorage

%global _description %{expand:
pulp-cli provides the "pulp" command, able to communicate with the Pulp3 API in
a more natural way than plain http. Specifically, resources can not only be
referenced by their href, but also their natural key (e.g. name). It also
handles waiting on tasks on behalf of the user.}

%description %_description


%prep
%autosetup -p1 -n pulp-cli-%{version}

# Remove the Python version upper bound to enable building with new versions in Fedora
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires test_requirements.txt


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


%check
%pyproject_check_import pulp_cli
%pytest -m help_page


%files -n pulp-cli -f %{pyproject_files}
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
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.36.0-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Thu Sep 04 2025 Matthias Dellweg <x9c4@redhat.com> - 0.36.0-1
- new version

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.34.0-3
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Matthias Dellweg <x9c4@redhat.com> - 0.34.0-1
- new version

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.32.1-3
- Rebuilt for Python 3.14

* Fri May 02 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.1-2
- Removed upper bound on required packaging. (thanks lbalhar)
- rebuilt

* Mon Apr 07 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.1-1
- new version

* Mon Apr 07 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.0-1
- new version

* Thu Mar 20 2025 Matthias Dellweg <x9c4@redhat.com> - 0.31.1-1
- new version
- Removed upper bound on build-required setuptools.

* Thu Feb 06 2025 Matthias Dellweg <x9c4@redhat.com> - 0.30.0-3
- Rebuilt without upper python version bound.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Matthias Dellweg <x9c4@redhat.com> - 0.30.0-1
- new version

* Tue Oct 22 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.2-4
- Bump setuptools build requirement.

* Wed Oct 09 2024 Lumír Balhar <lbalhar@redhat.com> - 0.29.2-3
- Allow newer tomli-w

* Wed Sep 25 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.2-2
- Added shell completion macros.

* Tue Sep 24 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.2-1
- new version

* Tue Sep 17 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.1-1
- new version

* Tue Sep 17 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.0-1
- Bump version to 0.29.0.

* Wed Sep 11 2024 Matthias Dellweg <x9c4@redhat.com> - 0.28.3-1
- Initial specfile
