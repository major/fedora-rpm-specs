%global module pamqp
Name:		python-%{module}
Version:	3.3.0
Release:	2%{?dist}
License:	BSD-3-Clause
Summary:	AMQP 0-9-1 library
URL:		https://github.com/gmr/%{module}
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz#/%{module}-%{version}.tar.gz
BuildArch:	noarch

%description
pamqp is a low level AMQP 0-9-1 frame encoding and decoding library for Python3.
pamqp is not a end-user client library for talking to RabbitMQ but rather is
used by client libraries for marshaling and unmarshaling AMQP frames.

%package -n python3-%{module}
Summary:	%{summary}
# python3-devel
BuildRequires:	pkgconfig(python3)
# python3-wheel
BuildRequires:	%{py3_dist wheel}
# python3-pytest
BuildRequires:	%{py3_dist pytest}
%{?python_provide:%python_provide python3-%{module}}

%description -n python3-%{module}
pamqp is a low level AMQP 0-9-1 frame encoding and decoding library for Python3.
pamqp is not a end-user client library for talking to RabbitMQ but rather is
used by client libraries for marshaling and unmarshaling AMQP frames.


%prep
%autosetup -n %{module}-%{version}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module}


%check
%{pytest}


%files -n python3-%{module} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 TI_Eugene <ti.eugene@gmail.com> - 3.3.0-1
- Version bump
- BR pyproject-rpm-macros removed
- Check section added

* Tue Aug 08 2023 TI_Eugene <ti.eugene@gmail.com> - 3.2.1-1
- Initial packaging
