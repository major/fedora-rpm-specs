Name:           python-opentelemetry-sdk-extension-aws
Version:        2.0.1
Release:        %autorelease -b 52
Summary:        AWS SDK extension for OpenTelemetry

# PyPI source distributions lacks tests; use the GitHub archive even though it
# includes many other packages maintained in the same repository
%global forgeurl https://github.com/open-telemetry/opentelemetry-python-contrib
# Having the equals character appear in the source filename breaks everything,
# and the build breaks because a source named %%{version}.tar.gz is not
# present. Using the url-escaped version of the tag is a workaround.
%global tag opentelemetry-sdk-extension-aws%%3D%%3D%{version}
# As a peculiarity of GitHub when the tag contains the equals character, the
# archive name (and the name of the directory containing the extracted sources)
# does not exactly match the tag.
%global extractdir opentelemetry-python-contrib-%(echo '%{tag}' | sed -r 's/(%%3D)+/-/')

License:        Apache-2.0
URL:            https://pypi.org/project/opentelemetry-sdk-extension-aws
Source:         %{forgeurl}/archive/%{tag}/%{extractdir}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Maintaining manual test dependencies is easier than trying to generate them
# from the top-level tox.ini.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-benchmark}

%global common_description %{expand:
This library provides components necessary to configure the OpenTelemetry SDK
for tracing with AWS X-Ray.}

%description %{common_description}


%package -n python3-opentelemetry-sdk-extension-aws
Summary:        %{summary}

%description -n python3-opentelemetry-sdk-extension-aws %{common_description}


%prep
%autosetup -n %{extractdir}


%generate_buildrequires
cd sdk-extension/opentelemetry-sdk-extension-aws
%pyproject_buildrequires -x test


%build
cd sdk-extension/opentelemetry-sdk-extension-aws
%pyproject_wheel


%install
cd sdk-extension/opentelemetry-sdk-extension-aws
%pyproject_install
# The opentelemetry and opentelemetry/sdk directies are shared
# namespace package directories; they are co-owned with other opentelemetry
# packages, including subpackages of python-opentelemetry and/or
# python-opentelemetry-contrib. See RHBZ#1935266.
%pyproject_save_files -l opentelemetry


%check
cd sdk-extension/opentelemetry-sdk-extension-aws
%pytest -v


%files -n python3-opentelemetry-sdk-extension-aws -f %{pyproject_files}
%doc sdk-extension/opentelemetry-sdk-extension-aws/README.rst


%changelog
%autochangelog
