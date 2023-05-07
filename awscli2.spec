%global pkgname aws-cli

Name:               awscli2
Version:            2.11.17
Release:            %autorelease

Summary:            Universal Command Line Environment for AWS, version 2
# all files are licensed under Apache-2.0, except:
# - awscli/topictags.py is MIT
# - awscli/botocore/vendored/six.py is MIT
License:            Apache-2.0 AND MIT
URL:                https://github.com/aws/aws-cli/tree/v2

Source0:            https://github.com/aws/aws-cli/archive/%{version}/%{pkgname}-%{version}.tar.gz

# ruamel-yaml 0.17.22 changed whitespace formatting, breaking some TestUpdateKubeconfig tests
# add a workaround for that until upstream comes with a proper fix
Patch0:             ruamel-yaml-0.17.22.patch

BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-pytest-xdist
BuildRequires:      python%{python3_pkgversion}-jsonschema
BuildRequires:      python-unversioned-command
BuildRequires:      procps-ng

Recommends:         groff

Provides:           awscli = %{version}-%{release}
Obsoletes:          awscli < 2

# provide an upgrade path from awscli-2 (Amazon Linux)
Provides:           awscli-2 = %{version}-%{release}
Obsoletes:          awscli-2 < %{version}-%{release}

# python-awscrt does not build on s390x
ExcludeArch:        s390x


%description
This package provides version 2 of the unified command line
interface to Amazon Web Services.


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# fix permissions
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +

# use unittest.mock
find -type f -name '*.py' -exec sed \
    -e 's/^\( *\)import mock$/\1from unittest import mock/' \
    -e 's/^\( *\)from mock import mock/\1from unittest import mock/' \
    -e 's/^\( *\)from mock import/\1from unittest.mock import/' \
    -i '{}' +


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files awscli

# remove unnecessary scripts
rm -vf %{buildroot}%{_bindir}/{aws_bash_completer,aws_zsh_completer.sh,aws.cmd}

# install shell completion
install -Dpm0644 bin/aws_bash_completer \
  %{buildroot}%{_datadir}/bash-completion/completions/aws
install -Dpm0644 bin/aws_zsh_completer.sh \
  %{buildroot}%{_datadir}/zsh/site-functions/_awscli


%check
# it appears that some tests modify the environment and remove PYTHONPATH
# so it's not passed to botocore cmd-runner, inject it here
sed -i '/self.driver.start(env=env)/i \ \ \ \ \ \ \ \ env["PYTHONPATH"] = "%{buildroot}%{python3_sitelib}"' \
    tests/utils/botocore/__init__.py

export TESTS_REMOVE_REPO_ROOT_FROM_PATH=1 TZ=UTC
%pytest --verbose --numprocesses=auto --dist=loadfile tests/unit tests/functional


%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/aws
%{_bindir}/aws_completer
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/aws
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_awscli


%changelog
%autochangelog
