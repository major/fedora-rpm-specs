%global pypi_name protobuf
%global pypi_version 6.33.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Protocol Buffers

License:        BSD-3-Clause
URL:            https://protobuf.dev
Source:         %{pypi_source}

Patch:          protobuf-unbundle-upb-and-utf8_range.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  gcc
BuildRequires:  protobuf-devel = %{pypi_version}
BuildRequires:  upb-static = %{pypi_version}

%description
Protocol buffers are Google's language-neutral,
platform-neutral, extensible mechanism for serializing
structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be
structured once, then you can use special generated
source code to easily write and read your structured
data to and from a variety of data streams and using
a variety of languages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Conflicts:      python3-%{pypi_name} < 4~~

%description -n python3-%{pypi_name}
Protocol buffers are Google's language-neutral,
platform-neutral, extensible mechanism for serializing
structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be
structured once, then you can use special generated
source code to easily write and read your structured
data to and from a variety of data streams and using
a variety of languages.

%prep
%autosetup -p1 -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled upb and utf8_range
rm -rf upb utf8_range

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# Uses google.protobuf but the macro does not support
# namespaced packages with a dot
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
# list files directly
%pyproject_save_files -l google

%check
# No tests shipped with sources on PyPI
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
