%global _enable_debug_package 0
%global debug_package %{nil}

Summary:            Synconf - Synclient configuration for Apple notebooks
Name:               synconf
Version:            0.0.1
Release:            1
License:            GPLv2+
Group:              User Interface/X Hardware Support
Source:             synconf-%{version}.tar.gz
URL:                http://github.com/orpiske/synconf
BuildArch:          noarch

%description
Synconf contains configuration files for synclient that reconfigure the driver
so that the touch pad for Apple notebooks (such as the Apple Macbook) will behave
like in OS X.

%prep
%setup -n %{name}-%{version}


%install
mkdir -p %{buildroot}/etc/X11/xorg.conf.d
make -f %{_builddir}/%{name}-%{version}/Makefile  PREFIX=%{buildroot}/etc/X11/xorg.conf.d install

%files
%config /etc/X11/xorg.conf.d/*

%changelog
* Sat Jul 9 2016 Otavio R. Piske <angusyoung@gmail.com> - 0.0.1
- Initial release

