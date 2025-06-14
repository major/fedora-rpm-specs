%bcond tests 1
# F43FailsToInstall: python3-google-cloud-storage
# https://bugzilla.redhat.com/show_bug.cgi?id=2371928
%bcond gcs 0
# Not packaged, and would have a tremendous number of dependencies.
%bcond moto 0

Name:           python-smart_open
Version:        7.1.0
Release:        %autorelease
Summary:        Utils for streaming large files (S3, HDFS, gzip, bz2, and more)

# SPDX
License:        MIT
URL:            https://github.com/piskvorky/smart_open
Source:         %{url}/archive/v%{version}/smart_open-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): %{shrink:
                                     %{?with_gcs:-x all}
                                     -x azure
                                     %{?with_gcs:-x gcs}
                                     -x http
                                     -x s3
                                     -x ssh
                                     -x webhdfs
                                     -x zst
                                     }
BuildOption(install):   -l smart_open

%if %{with tests}
# See tests_require in setup.py.
%if %{with moto}
BuildRequires:  %{py3_dist moto[server]}
%endif
BuildRequires:  %{py3_dist responses}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-rerunfailures}
# The dependencies on pytest_benchmark, awscli, pyopenssl, and numpy were all
# added in upstream commit 8a58abe5e751af5b72e219e1bf3a90bb54e13b12.
# - Not needed; we do not care about benchmarks.
# BuildRequires:  %%{py3_dist pytest_benchmark}
# - Not required for any tests that we can run (if at all)
# BuildRequires:  %%{py3_dist awscli}
# - Not required for any tests that we can run (if at all)
# BuildRequires:  %%{py3_dist pyopenssl}
# - This one is real: used by integration-tests/test_207.py
BuildRequires:  %{py3_dist numpy}
%endif

BuildArch:      noarch

%global common_description %{expand:
smart_open is a Python library for efficient streaming of very large files
from/to storages such as S3, GCS, Azure Blob Storage, HDFS, WebHDFS, HTTP,
HTTPS, SFTP, or local filesystem. It supports transparent, on-the-fly
(de-)compression for a variety of different formats.

smart_open is a drop-in replacement for Pythons built-in open(): it can do
anything open can (100% compatible, falls back to native open wherever
possible), plus lots of nifty extra stuff on top.}

%description %{common_description}


%package -n python3-smart-open
Summary:        %{summary}

%if %[ %{defined fc42} || %{defined fc41} ]
# For backwards compatibility with old manual Requires
Requires:       python3-smart-open+s3 = %{version}-%{release}
Requires:       python3-smart-open+http = %{version}-%{release}
%endif

# The source package is named python-smart_open for historical reasons.The
# binary package, python3-smart-open, is named using the canonical project
# name[1]; see also [2].
#
# The %%py_provides macro is used to provide an upgrade path from
# python3-smart_open and to produce the appropriate Provides for the importable
# module[3].
#
# [1] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_canonical_project_name
# [2] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# [3] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules

# Provide an upgrade path; we can remove this after Fedora 45.
%py_provides python3-smart_open
Obsoletes:      python3-smart_open < 7.1.0-5

%description -n python3-smart-open %{common_description}


%if %{with gcs}
%pyproject_extras_subpkg -n python3-smart-open all gcs
%endif
%pyproject_extras_subpkg -n python3-smart-open azure http s3 ssh webhdfs zst


%check -a
%if %{with tests}
%if %{without gcs}
ignore="${ignore-} --ignore=smart_open/tests/test_gcs.py"
%endif
%if %{without moto}
ignore="${ignore-} --ignore=smart_open/tests/test_s3_version.py"
ignore="${ignore-} --ignore=smart_open/tests/test_s3.py"
ignore="${ignore-} --ignore=smart_open/tests/test_smart_open.py"
%endif

%pytest ${ignore-} -rs
%endif


%files -n python3-smart-open -f %{pyproject_files}
%doc CHANGELOG.md
%doc MIGRATING_FROM_OLDER_VERSIONS.rst
%doc README.rst
%doc help.txt
%doc howto.md


%changelog
%autochangelog
