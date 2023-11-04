%global pypi_name extractcode

Name:           python-%{pypi_name}
Version:        31.0.0
Release:        %autorelease
Summary:        File extraction library and CLI tool to extract almost any archive

License:        Apache-2.0 AND MIT
URL:            https://github.com/nexB/extractcode
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# setup.cfg: fix invalid version spec
Patch:          %url/commit/6270a8805c7fb964e545a56ca8a92829d240a96a.patch
Patch:          %url/pull/55.patch
Patch:          %url/pull/56.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(extractcode-7z-system-provided)
BuildRequires:  python3dist(extractcode-libarchive-system-provided)
BuildRequires:  python3dist(typecode-libmagic-system-provided)

%global common_description %{expand:
A mostly universal file extraction library and CLI tool to extract almost any
archive in a reasonably safe way on Linux, macOS and Windows.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(extractcode-7z-system-provided)
Recommends:     python3dist(extractcode-libarchive-system-provided)
Recommends:     python3dist(typecode-libmagic-system-provided)

%description -n python3-%{pypi_name} %{common_description}

%pyproject_extras_subpkg -n python3-%{pypi_name} full

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i 's|extractcode-7z >= 16.5.210525|extractcode-7z-system-provided|' setup.cfg
sed -i 's|extractcode_libarchive >= 3.5.1.210525|extractcode_libarchive-system-provided|' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# TestExtractVmImage needs access to kernel
# Then https://github.com/nexB/extractcode/issues/53
%pytest -k 'not TestExtractVmImage and not test_get_extractor_qcow2 and not test_extract_rar_with_trailing_data and not test_extractcode_command_can_take_an_empty_directory and not test_extractcode_command_does_extract_verbose and not test_extractcode_command_always_shows_something_if_not_using_a_tty_verbose_or_not and not test_extractcode_command_works_with_relative_paths and not test_extractcode_command_works_with_relative_paths_verbose and not test_usage_and_help_return_a_correct_script_name_on_all_platforms and not test_extractcode_command_can_extract_archive_with_unicode_names_verbose and not test_extractcode_command_can_extract_archive_with_unicode_names and not test_extractcode_command_can_extract_shallow and not test_extractcode_command_can_ignore and not test_extractcode_command_does_not_crash_with_replace_originals_and_corrupted_archives and not test_extractcode_command_can_extract_nuget'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst
%{_bindir}/extractcode

%files -n python-%{pypi_name}-doc
%doc html
%changelog
%autochangelog
