
-- this function is called when the box is initialized
function initialize(box)

	dofile(box:get_config("${Path_Data}") .. "/plugins/stimulation/lua-stimulator-stim-codes.lua")


end

-- this function is called when the box is uninitialized
function uninitialize(box)
	io.write("uninitialize has been called\n")
end

-- this function is called once by the box
function process(box)
	local t=0

 	box:send_stimulation(1, OVTK_StimulationId_ExperimentStart, t, 0)
	t = t + 5

	box:send_stimulation(1, OVTK_StimulationId_Beep, t, 0)
	t = t + 2

	box:send_stimulation(1, OVTK_StimulationId_BaselineStart, t, 0)
	-- t = t + 1/64

        box:send_stimulation(1, OVTK_GDF_Feedback_Continuous, t, 0)
	t = t + 60

	box:send_stimulation(1, OVTK_StimulationId_BaselineStop, t, 0)
	t = t + 5

	box:send_stimulation(1, OVTK_GDF_End_Of_Session, t, 0)
    	t = t + 5

	box:send_stimulation(1, OVTK_StimulationId_Train, t, 0)
    	t = t + 1
    
    
    	box:send_stimulation(1, OVTK_StimulationId_ExperimentStop, t, 0)
end
