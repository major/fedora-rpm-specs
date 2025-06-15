Name:           python-irodsclient
Version:        3.1.1
Release:        %autorelease
Summary:        A python API for iRODS

# SPDX
License:        BSD-3-Clause
URL:            https://github.com/irods/python-irodsclient
Source0:        %{pypi_source python-irodsclient}
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        prc_write_irodsA.py.1

BuildSystem:            pyproject
BuildOption(install):   -l irods
# * The test runner module requires xmlrunner, which is no longer packaged.
# * Merely importing ssl_test_client requires configured iRODS credentials.
BuildOption(check): -e irods.test.runner -e irods.test.ssl_test_client
# All tests require network access and a valid account on a running iRODS grid.
# See irods/test/README.rst.

BuildArch:      noarch

%global common_description %{expand:
iRODS (https://www.irods.org/) is an open source distributed data management
system. This is a client API implemented in Python.}

%description %{common_description}


%package -n python3-irodsclient
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-irods

%description -n python3-irodsclient %{common_description}


%install -a
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'
%py3_shebang_fix '%{buildroot}%{_bindir}/prc_write_irodsA.py'

# Remove useless shebangs in files that were be installed without executable
# permission. The pattern of selecting files before modifying them with sed
# keeps us from unnecessarily discarding the original mtimes on unmodified
# files. Note that we must not do this in %%prep because we want to strip the
# shebang from the copy of prc_write_irodsA.py in site-packages, but not from
# the copy in %%{_bindir}.
find '%{buildroot}%{python3_sitelib}/irods' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'


%files -n python3-irodsclient -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%{_bindir}/prc_write_irodsA.py
%{_mandir}/man1/prc_write_irodsA.py.1*


%changelog
%autochangelog
