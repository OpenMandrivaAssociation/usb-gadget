Name:		usb-gadget
Summary:	Tool to automatically configure USB gadget ports
Version:	1.0
Release:	1
Source0:	usb-gadget
Source1:	usb-gadget.service
License:	GPLv3

%description
Tool to automatically configure USB gadget ports

%prep

%build

%install
mkdir -p %{buildroot}%{_sbindir} \
	%{buildroot}/lib/systemd/system
install -c -m 755 %{S:0} %{buildroot}%{_sbindir}/
install -c -m 644 %{S:1} %{buildroot}/lib/systemd/system/

%files
%{_sbindir}/usb-gadget
/lib/systemd/system/usb-gadget.service
