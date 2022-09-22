%global srcname visidata

Name:           %{srcname}
Version:        2.8
Release:        %autorelease
Summary:        Terminal interface for exploring and arranging tabular data

License:        GPLv3
URL:            https://visidata.org
Source0:        %pypi_source
# https://github.com/saulpw/visidata/pull/269
Patch0001:      0001-Remove-extra-copy-of-man-page.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

Requires:       python3-%{srcname} = %{version}-%{release}

%description
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.


%package -n     python3-%{srcname}
Summary:        %{summary}

# Optional dependencies
Recommends: python3dist(PyYAML)
Recommends: python3dist(datapackage)
Recommends: python3dist(dnslib)
Recommends: python3dist(dpkt)
Recommends: python3dist(fonttools)
Recommends: python3dist(h5py)
Recommends: python3dist(lxml)
Recommends: python3dist(mapbox-vector-tile)
Recommends: python3dist(namestand)
Recommends: python3dist(numpy)
Recommends: python3dist(openpyxl)
Recommends: python3dist(pandas) >= 0.19.2
Recommends: python3dist(pdfminer-six)
Recommends: python3dist(psycopg2)
Recommends: python3dist(pypng)
Recommends: python3dist(pyshp)
Recommends: python3dist(requests)
Recommends: python3dist(sas7bdat)
Recommends: python3dist(savReaderWriter)
Recommends: python3dist(tabulate)
Recommends: python3dist(vobject)
Recommends: python3dist(wcwidth)
Recommends: python3dist(xlrd)
Recommends: python3dist(xport)

%description -n python3-%{srcname}
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files
%{_bindir}/visidata
%{_bindir}/vd
%{_mandir}/man1/vd.1*
%{_mandir}/man1/visidata.1*

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.gpl3

%changelog
%autochangelog
