%global         forgeurl https://github.com/pyeve/events

Name:           python-events
Version:        0.5
%forgemeta
Release:        %autorelease
Summary:        Bringing the elegance of C# EventHandler to Python

License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Bringing the elegance of C EventHandler to Python The C language provides a
handy way to declare, subscribe to and fire events. Technically, an event is a
"slot" where callback functions (event handlers) can be attached to a process
referred to as subscribing to an event. Here is a handy package that
encapsulates the core to event subscription and event firing and feels like a
"natural"}

%description    %_description


%package -n     python3-events
Summary:        %{summary}

%description -n python3-events %_description


%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l events


%check
%pytest events/tests/tests.py


%files -n python3-events -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
