Name:           python-webdav4
Version:        0.10.0
Release:        %autorelease
Summary:        WebDAV client library with an fsspec-based filesystem and a CLI

# SPDX
License:        MIT
URL:            https://github.com/skshetry/webdav4
Source0:        %{pypi_source webdav4}

# Hand-written for Fedora in groff_man(7) format using --help output
Source10:       dav.1
Source11:       dav-cat.1
Source12:       dav-cp.1
Source13:       dav-du.1
Source14:       dav-ls.1
Source15:       dav-mkdir.1
Source16:       dav-mv.1
Source17:       dav-rm.1
Source18:       dav-run.1
Source19:       dav-sync.1

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x all,fsspec,http2,tests
BuildOption(install):   -l webdav4

BuildArch:      noarch

BuildRequires:  tomcli

%global common_description %{expand:
Webdav API with an (optional) fsspec implementation and a CLI.}

%description %{common_description}


%package -n python3-webdav4
Summary:        %{summary}

# Provides colorized terminal output in the CLI
Recommends:     %{py3_dist colorama}

%description -n python3-webdav4 %{common_description}


%pyproject_extras_subpkg -n python3-webdav4 fsspec http2


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.tests 'pytest-cov*'
tomcli set pyproject.toml str tool.pytest.ini_options.addopts -- "$(
  tomcli get pyproject.toml tool.pytest.ini_options.addopts |
  sed -r 's/--cov[^[:blank:]]*//g')"


%install -a
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE15}' '%{SOURCE16}' '%{SOURCE17}' '%{SOURCE18}' '%{SOURCE19}'


%check -a
%pytest ${ignore-} -rs -vv


%files -n python3-webdav4 -f %{pyproject_files}
%doc README.md

%{_bindir}/dav
%{_mandir}/man1/dav.1*
%{_mandir}/man1/dav-*.1*


%changelog
%autochangelog
