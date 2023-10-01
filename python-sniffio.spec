Name:           python-sniffio
Version:        1.3.0
Release:        %autorelease
Summary:        Sniff out which async library your code is running under
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/sniffio
Source:         %{pypi_source sniffio}
BuildArch:      noarch

%global common_description %{expand:
You're writing a library.  You've decided to be ambitious, and support multiple
async I/O packages, like Trio, and asyncio, and ... You've written a bunch of
clever code to handle all the differences.  But... how do you know which piece
of clever code to run?  This is a tiny package whose only purpose is to let you
detect which async library your code is running under.}


%description %{common_description}


%package -n python3-sniffio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}


%description -n python3-sniffio %{common_description}


%prep
%autosetup -n sniffio-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sniffio


%check
# curio is upstream discontinued and is not yet available for Python 3.12
%pytest --verbose -k "not test_curio"


%files -n python3-sniffio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
