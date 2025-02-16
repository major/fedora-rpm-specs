%global pkgname aws-cli

Name:               awscli2
Version:            2.24.4
Release:            %autorelease

Summary:            Universal Command Line Environment for AWS, version 2
# all files are licensed under Apache-2.0, except:
# - awscli/topictags.py is MIT
# - awscli/botocore/vendored/six.py is MIT
License:            Apache-2.0 AND MIT
URL:                https://github.com/aws/aws-cli/tree/v2

Source0:            https://github.com/aws/aws-cli/archive/%{version}/%{pkgname}-%{version}.tar.gz

# adapt to whitespace formatting changes and removal of OrderedDict in ruamel-yaml
Patch0:             ruamel-yaml-0.17.32.patch
# fix Python 3.12 incompatibilities
Patch1:             python312.patch
# fix incorrect assertions in TestKubeconfigLoader
Patch2:             assertions.patch
# Bump ceiling for botocore memory leak tests
# https://github.com/aws/aws-cli/pull/8744
# https://github.com/boto/botocore/issues/3205
Patch3:             0001-Bump-the-ceiling-for-botocore-memory-leak-tests-to-1.patch
# compatibility fixes for urllib3 v2
Patch4:             urllib3-v2.patch

BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python-unversioned-command
BuildRequires:      procps-ng

Recommends:         groff

Provides:           bundled(python3dist(botocore)) = 2.0.0
Provides:           bundled(python3dist(s3transfer)) = 0.5.1

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

# remove version caps on dependencies
sed -i 's/,<=\?[^"]*"/"/' pyproject.toml

# loosen awscrt version requirement
sed -i 's/awscrt==/awscrt>=/' pyproject.toml

# remove zipp dependency
sed -i "/zipp<3.21.0/d" pyproject.toml

# use unittest.mock
find -type f -name '*.py' -exec sed \
    -e 's/^\( *\)import mock$/\1from unittest import mock/' \
    -e 's/^\( *\)from mock import mock/\1from unittest import mock/' \
    -e 's/^\( *\)from mock import/\1from unittest.mock import/' \
    -i '{}' +

# Fedora does not run coverage tests.
# mock is deprecated in Fedora. We use unittest.mock.
# pip-tools is not used directly by the unit tests.
# pytest-xdist is unwanted in RHEL.
sed \
    -e 's|==.*||' \
    -e '/coverage/d' \
    -e '/mock/d' \
    -e '/pip-tools/d' \
    -e '/pytest-cov/d' \
    %{?rhel:-e '/pytest-xdist/d'} \
    requirements-test.txt > _requirements-test.txt


%generate_buildrequires
%pyproject_buildrequires _requirements-test.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files awscli

# remove unnecessary scripts
rm -vf %{buildroot}%{_bindir}/{aws_bash_completer,aws_zsh_completer.sh,aws.cmd}

# install shell completion
install -Dpm0644 bin/aws_bash_completer \
  %{buildroot}%{bash_completions_dir}/aws
install -Dpm0644 bin/aws_zsh_completer.sh \
  %{buildroot}%{zsh_completions_dir}/_awscli


%check
# it appears that some tests modify the environment and remove PYTHONPATH
# so it's not passed to botocore cmd-runner, inject it here
sed -i '/self.driver.start(env=env)/i \ \ \ \ \ \ \ \ env["PYTHONPATH"] = "%{buildroot}%{python3_sitelib}"' \
    tests/utils/botocore/__init__.py

export TESTS_REMOVE_REPO_ROOT_FROM_PATH=1 TZ=UTC
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
%pytest --verbose %{!?rhel:--numprocesses=auto --dist=loadfile --maxprocesses=4} tests/unit tests/functional


%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/aws
%{_bindir}/aws_completer
%{bash_completions_dir}/aws
%{zsh_completions_dir}/_awscli


%changelog
%autochangelog
